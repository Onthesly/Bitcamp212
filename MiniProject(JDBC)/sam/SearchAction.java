package net.bit.sam;

import java.util.Scanner;

public class SearchAction implements Action {
	@Override
	public void execute(Scanner sc) {
		System.out.println("�˻��� ����� id�� �Է��ϼ���");
		System.out.print("���id : ");
		int id = Integer.parseInt(sc.nextLine());
		
		SamDAO samDAO = new SamDAO();
		SamDTO temp = new SamDTO(id, null, null);
		SamDTO general = samDAO.getSam(temp);
		if(general == null) {
			System.out.println("����� �������� �ʽ��ϴ�\n");
			return;
		} else {
			SamDTO samList = samDAO.searchSam(general);
			System.out.println("--------------------------------------------------------------------------------------------------");
			System.out.println("id : " + samList.getId()
				+ ",    �̸� : " + samList.getName()
				+ ",    ���� : " + samList.getCountry()
				+ ",    ��� : " + samList.getGrade()
				+ ",    ���� : " + samList.getSpeciality()
				+ ",    ��� : " + samList.getGeneralship()
				+ ",    ���� : " + samList.getStrength()
				+ ",    ���� : " + samList.getIntellect());
			System.out.println("--------------------------------------------------------------------------------------------------\n");
		}
	}
	
}
