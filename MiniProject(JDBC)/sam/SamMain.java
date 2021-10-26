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
			System.out.println("다음 메뉴 중 하나를 입력하세요");
			System.out.print("1.장수 추가  ");
			System.out.print("2.장수 목록 보기  ");
			System.out.print("3.장수 삭제  ");
			System.out.print("4.장수 정보 수정  ");
			System.out.print("5.장수 상세 보기  ");
			System.out.print("9.종료 >>> ");
			
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
				System.out.println("종료합니다");
				isStop = true;	
			}
		}
		while(!isStop);
	}

}
