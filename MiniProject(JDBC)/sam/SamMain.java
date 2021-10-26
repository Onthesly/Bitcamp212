package net.bit.sam;

import java.util.Scanner;

public class SamMain {
	
	static SamDTO[] samGenerals;
	public static void main(String[] args) {
		SamService samService = new SamService();
		Scanner sc = new Scanner(System.in);
		samGenerals = new SamDTO[0];
		boolean isStop = false;
		do {
			System.out.println("���� �޴� �� �ϳ��� �Է��ϼ���");
			System.out.print("1.��� �߰�  ");
			System.out.print("2.��� ��� ����  ");
			System.out.print("3.��� ����  ");
			System.out.print("4.��� ���� ����  ");
			System.out.print("5.��� �� ����  ");
			System.out.print("9.���� >>> ");
			
			String command = sc.nextLine();
			switch (command) {
			case "1":
				AddAction addAction = new AddAction();
				samService.process(addAction, sc);
				break;
			case "2":
				ListAction listAction = new ListAction();
				samService.process(listAction, sc);
				break;
			case "3":
				DeleteAction deleteAction = new DeleteAction();
				samService.process(deleteAction, sc);
				break;	
			case "4":
				UpdateAction updateAction = new UpdateAction();
				samService.process(updateAction, sc);
				break;
			case "5":
				SearchAction searchAction = new SearchAction();
				samService.process(searchAction, sc);
				break;	
			case "9":
				System.out.println("�����մϴ�");
				isStop = true;	
			}
		}
		while(!isStop);
	}

}
