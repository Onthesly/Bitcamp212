package net.bit.sam;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.SQLIntegrityConstraintViolationException;
import java.sql.Statement;
import java.util.ArrayList;

public class SamDAO {
	private Connection conn = null;
	private PreparedStatement stmt = null;
	private Statement stmt2 = null;
	private ResultSet rs = null;
	
	private final String SAM_INSERT = "insert all into samgeneral values (?, ?, ?) into samgeneralstat values (?, ?, ?, ?, ?, ?) select * from dual" ;
//	private final String SAM_UPDATE = "update samgeneral set name=?, country=? where id=?";
	private final String SAM_DELETE = "delete from samgeneral where id=?";
	private final String SAM_GET = "select * from samgeneral where id=?";
	private final String SAM_LIST = "select * from samgeneral order by id";
	private final String SAM_SEARCH = "select a.*, b.grade, b.speciality, b.generalship, b.strength, b.intellect from samgeneral a, samgeneralstat b where a.id = b.id and a.name=?";
	
	public void insertSam(SamDTO dto) {
		try {
			conn = SamDB.getConnection();
			stmt = conn.prepareStatement(SAM_INSERT);
			stmt.setInt(1, dto.getId());
			stmt.setString(2, dto.getName());
			stmt.setString(3, dto.getCountry());
			stmt.setInt(4, dto.getId());
			stmt.setString(5, dto.getGrade());
			stmt.setString(6, dto.getSpeciality());
			stmt.setInt(7, dto.getGeneralship());
			stmt.setInt(8, dto.getStrength());
			stmt.setInt(9, dto.getIntellect());
			stmt.executeUpdate();
			System.out.println("성공적으로 등록되었습니다\n");
		} catch (SQLIntegrityConstraintViolationException sqle) {
			System.out.println("!!오류 : ID중복!!\n");
			return;
		} catch (SQLException sqle2) {
			System.out.println("!!오류 : 입력형식이 올바르지 않습니다!!\n");
			return;
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			SamDB.close(stmt, conn);
		}
	}//insertSam end
	
	
	public void updateSam(SamDTO dto) {
		try {
			conn = SamDB.getConnection();
			stmt2 = conn.createStatement();
			stmt2.addBatch("update samgeneral set name='" + dto.getName() + "', country='" + dto.getCountry() + "' where id=" + dto.getId());
			stmt2.addBatch("update samgeneralstat set grade='" + dto.getGrade() + "', speciality='" + dto.getSpeciality()
				+ "', generalship='" + dto.getGeneralship() + "', strength='" + dto.getStrength()
				+ "', intellect='" + dto.getIntellect() + "' where id=" + dto.getId());
			stmt2.executeBatch();
			conn.commit();
			System.out.println("성공적으로 수정되었습니다\n");
		} catch (SQLException sqle2) {
			System.out.println("!!오류 : 입력형식이 올바르지 않습니다!!\n");
			return;
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			SamDB.close(stmt2, conn);
		}
	}//updateSam end
	
	
	public void deleteSam(SamDTO dto) {
		try {
			conn = SamDB.getConnection();
			stmt = conn.prepareStatement(SAM_DELETE);
			stmt.setInt(1, dto.getId());
			stmt.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			SamDB.close(stmt, conn);
		}
	}//deleteSam end
	
	
	public SamDTO getSam(SamDTO temp) {
		SamDTO general = null;
		
		try {
			conn = SamDB.getConnection();
			stmt = conn.prepareStatement(SAM_GET);
			stmt.setInt(1, temp.getId());
			rs = stmt.executeQuery();
			if(rs.next()) {
				int id = rs.getInt("id");
				String name = rs.getString("name");
				String country = rs.getString("country");
				general = new SamDTO(id, name, country);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			SamDB.close(stmt, conn);
		}
		
		return general;
	}//getSam end
	
	
	public SamDTO searchSam(SamDTO temp) {
		SamDTO general = null;
				
		try {
			conn = SamDB.getConnection();
			stmt = conn.prepareStatement(SAM_SEARCH);
			stmt.setString(1, temp.getName());
			rs = stmt.executeQuery();
			if(rs.next()) {
				int id = rs.getInt("id");
				String name = rs.getString("name");
				String country = rs.getString("country");
				String grade = rs.getString("grade");
				String speciality = rs.getString("speciality");
				int generalship = rs.getInt("generalship");
				int strength = rs.getInt("strength");
				int intellect = rs.getInt("intellect");
				general = new SamDTO(id, name, country, grade, speciality, generalship, strength, intellect);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			SamDB.close(stmt, conn);
		}
		
		return general;
	}//searchSam end
	
	public ArrayList<SamDTO> getSamList(SamDTO dto) {
		SamDTO samGeneral = null;
		ArrayList<SamDTO> samList = new ArrayList<SamDTO>();
		
		try {
			conn = SamDB.getConnection();
			stmt = conn.prepareStatement(SAM_LIST);
			rs = stmt.executeQuery();
			while(rs.next()) {
				int id = rs.getInt("id");
				String name = rs.getString("name");
				String country = rs.getString("country");
				samGeneral = new SamDTO(id, name, country);
				samList.add(samGeneral);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			SamDB.close(rs, stmt, conn);
		}
		
		return samList;
	}//getSamList end
}
