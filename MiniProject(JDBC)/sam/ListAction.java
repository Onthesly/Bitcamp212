package net.bit.sam;

import java.util.ArrayList;
import java.util.Scanner;

public class ListAction implements Action {
	@Override
	public void execute(Scanner sc) {
		SamDAO samDAO = new SamDAO();
		ArrayList<SamDTO> samList = samDAO.getSamList(null);
		if (samList.size() >= 1) {
			System.out.println("--------------------------------------------------------------------------------------------------");
			for (SamDTO general : samList) {
				System.out.println("ID : " + general.getId()
					+ ", \t�̸� : " + general.getName()
					+ ",\t���� : " + general.getCountry());
			}
			System.out.println("--------------------------------------------------------------------------------------------------");
			System.out.println();
		} else {
			System.out.println("��� ������ �������� �ʽ��ϴ�");
		}
	}
}
