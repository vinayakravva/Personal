
public class dollarPattern {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for(int i=1;i<=4;i++) {
			if(i==1 || i==4) {
				for(int j=0;j<4;j++) {
					System.out.print("$");
					
				}
				System.out.println();
				
			}
		   else {
			for(int k=1;k<5;k++) {
				if(k==1 ||k==4) {
					System.out.print("$");
				}
				else {
					System.out.print(" ");
				}
			}
			System.out.println();
		}

	}

}
}
