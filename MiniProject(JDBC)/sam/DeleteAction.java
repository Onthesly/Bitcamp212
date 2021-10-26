package net.bit.sam;

import java.util.Scanner;

public class DeleteAction implements Action {
	@Override
	public void execute(Scanner sc) {
		System.out.println("삭제할 장수의 id를 입력하세요");
		System.out.print("장수id : ");
		int id = Integer.parseInt(sc.nextLine());
		
		SamDTO general = new SamDTO(id, null, null);
		deleteGeneral(general);
		System.out.println("성공적으로 삭제되었습니다\n");
	}
	
	private void deleteGeneral(SamDTO general) {
		SamDAO samDAO = new SamDAO();
		samDAO.deleteSam(general);
	}
}
