package net.bit.sam;

import java.util.Scanner;

public class AddAction implements Action {
	@Override
	public void execute(Scanner sc) {
		System.out.println("����� ����� ������ �Է��ϼ���");
		System.out.print("ID : ");
		int id = Integer.parseInt(sc.nextLine());
		SamDAO samDAO = new SamDAO();
		SamDTO temp = new SamDTO(id, null, null);
		SamDTO temp2 = samDAO.getSam(temp);
		if (temp2 != null) {
			System.out.println("�̹� ����� �����մϴ�\n");
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
			
			SamDTO general = new SamDTO(id, name, country, grade, speciality, generalship, strength, intellect);
			addGeneral(general);
		}
	}
	
	private void addGeneral(SamDTO general) {
		SamDAO samDAO = new SamDAO();
		samDAO.insertSam(general);
	}
}
