package net.bit.sam;

import java.util.Scanner;

public class DeleteAction implements Action {
	@Override
	public void execute(Scanner sc) {
		System.out.println("������ ����� id�� �Է��ϼ���");
		System.out.print("���id : ");
		int id = Integer.parseInt(sc.nextLine());
		
		SamDTO general = new SamDTO(id, null, null);
		deleteGeneral(general);
		System.out.println("���������� �����Ǿ����ϴ�\n");
	}
	
	private void deleteGeneral(SamDTO general) {
		SamDAO samDAO = new SamDAO();
		samDAO.deleteSam(general);
	}
}
