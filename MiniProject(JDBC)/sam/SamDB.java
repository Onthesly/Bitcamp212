package net.bit.sam;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class SamDB {
	
	public static Connection getConnection() {
		try {
			String driver = "oracle.jdbc.driver.OracleDriver";
			String url = "jdbc:oracle:thin:@127.0.0.1:1521:XE";
			String user = "system";
			String password = "1234";
			Class.forName(driver);
			return DriverManager.getConnection(url, user, password);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return null;
	}
	
	public static void close(PreparedStatement stmt, Connection conn) {
		try {
			if(stmt != null) stmt.close();
			if(conn != null) conn.close();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			stmt = null;
			conn = null;
		}
	}
	
	public static void close(Statement stmt2, Connection conn) {
		try {
			if(stmt2 != null) stmt2.close();
			if(conn != null) conn.close();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			stmt2 = null;
			conn = null;
		}
	}
	
	public static void 	close(ResultSet rs, PreparedStatement stmt, Connection conn) {
		try {
			if(rs != null) rs.close();
			if(stmt != null) stmt.close();
			if(conn != null) conn.close();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			rs = null;
			stmt = null;
			conn = null;
		}
	}
}
