package net.bit.sam;

import java.util.Scanner;

public class UpdateAction implements Action {
	@Override
	public void execute(Scanner sc) {
		System.out.println("수정할 장수의 id를 입력하세요");
		System.out.print("장수id : ");
		int id = Integer.parseInt(sc.nextLine());
		
		SamDAO samDAO = new SamDAO();
		SamDTO temp = new SamDTO(id, null, null);
		SamDTO general = samDAO.getSam(temp);
		SamDTO generalUp = new SamDTO(id, null, null, null, null, 0, 0, 0);
		if(general == null) {
			System.out.println("수정할 장수가 존재하지 않습니다");
			return;
		} else {
			System.out.print("이름 : ");
			String name = sc.nextLine();
			System.out.print("국가 : ");
			String country = sc.nextLine();
			System.out.print("등급 : ");
			String grade = sc.nextLine();
			System.out.print("병과 : ");
			String speciality = sc.nextLine();
			System.out.print("통솔 : ");
			int generalship = Integer.parseInt(sc.nextLine());
			System.out.print("무력 : ");
			int strength = Integer.parseInt(sc.nextLine());
			System.out.print("지력 : ");
			int intellect = Integer.parseInt(sc.nextLine());
			
			generalUp.setName(name);
			generalUp.setCountry(country);
			generalUp.setGrade(grade);
			generalUp.setSpeciality(speciality);
			generalUp.setGeneralship(generalship);
			generalUp.setStrength(strength);
			generalUp.setIntellect(intellect);
		}
		updateGeneral(generalUp);
	}
	
	private void updateGeneral(SamDTO generalUp) {
		SamDAO samDAO = new SamDAO();
		samDAO.updateSam(generalUp);
	}
}
