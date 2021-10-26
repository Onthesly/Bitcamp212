package net.bit.sam;

import java.util.Scanner;

public class SamService {
	void process(Action action, Scanner sc) {
		action.execute(sc);
	}
}
