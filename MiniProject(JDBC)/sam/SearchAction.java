package net.bit.sam;

import java.util.Scanner;

public class SearchAction implements Action {
	@Override
	public void execute(Scanner sc) {
		System.out.println("검색할 장수의 id를 입력하세요");
		System.out.print("장수id : ");
		int id = Integer.parseInt(sc.nextLine());
		
		SamDAO samDAO = new SamDAO();
		SamDTO temp = new SamDTO(id, null, null);
		SamDTO general = samDAO.getSam(temp);
		if(general == null) {
			System.out.println("장수가 존재하지 않습니다\n");
			return;
		} else {
			SamDTO samList = samDAO.searchSam(general);
			System.out.println("--------------------------------------------------------------------------------------------------");
			System.out.println("id : " + samList.getId()
				+ ",    이름 : " + samList.getName()
				+ ",    국가 : " + samList.getCountry()
				+ ",    등급 : " + samList.getGrade()
				+ ",    병과 : " + samList.getSpeciality()
				+ ",    통솔 : " + samList.getGeneralship()
				+ ",    무력 : " + samList.getStrength()
				+ ",    지력 : " + samList.getIntellect());
			System.out.println("--------------------------------------------------------------------------------------------------\n");
		}
	}
	
}
