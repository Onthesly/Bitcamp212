package net.bit.sam;

import java.util.Scanner;

public class AddAction implements Action {
	@Override
	public void execute(Scanner sc) {
		System.out.println("등록할 장수의 정보를 입력하세요");
		System.out.print("ID : ");
		int id = Integer.parseInt(sc.nextLine());
		SamDAO samDAO = new SamDAO();
		SamDTO temp = new SamDTO(id, null, null);
		SamDTO temp2 = samDAO.getSam(temp);
		if (temp2 != null) {
			System.out.println("이미 장수가 존재합니다\n");
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
			
			SamDTO general = new SamDTO(id, name, country, grade, speciality, generalship, strength, intellect);
			addGeneral(general);
		}
	}
	
	private void addGeneral(SamDTO general) {
		SamDAO samDAO = new SamDAO();
		samDAO.insertSam(general);
	}
}
