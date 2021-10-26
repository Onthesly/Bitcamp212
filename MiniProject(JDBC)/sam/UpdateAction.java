package net.bit.sam;

import java.util.Scanner;

public class UpdateAction implements Action {
	@Override
	public void execute(Scanner sc) {
		System.out.println("������ ����� id�� �Է��ϼ���");
		System.out.print("���id : ");
		int id = Integer.parseInt(sc.nextLine());
		
		SamDAO samDAO = new SamDAO();
		SamDTO temp = new SamDTO(id, null, null);
		SamDTO general = samDAO.getSam(temp);
		SamDTO generalUp = new SamDTO(id, null, null, null, null, 0, 0, 0);
		if(general == null) {
			System.out.println("������ ����� �������� �ʽ��ϴ�");
			return;
		} else {
			System.out.print("�̸� : ");
			String name = sc.nextLine();
			System.out.print("���� : ");
			String country = sc.nextLine();
			System.out.print("��� : ");
			String grade = sc.nextLine();
			System.out.print("���� : ");
			String speciality = sc.nextLine();
			System.out.print("��� : ");
			int generalship = Integer.parseInt(sc.nextLine());
			System.out.print("���� : ");
			int strength = Integer.parseInt(sc.nextLine());
			System.out.print("���� : ");
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
