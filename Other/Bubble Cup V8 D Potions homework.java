import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
	public static void main(String args[]) throws IOException {
		//get values
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int numInput = Integer.parseInt(reader.readLine());
		int[] values = new int[numInput];
		for (int i = 0; i < numInput; i++) {
			values[i] = Integer.parseInt(reader.readLine());
		}
		
		//sort values from min to max
		Arrays.sort(values);
		
		//print sorted values
		/*for (int i = 0; i < numInput; i++) {
			System.out.println(values[i]);
		}*/
		
		//sum values
		//int sum = 0;
		long result = 0;
		//int n = numInput - 1;
		for (int a = 0; a < numInput; a++) {
			//sum += (values[a])*(values[n]);
			result += ((values[a]%10007)*(values[numInput - 1 - a]) %10007);
			//System.out.println(values[a] + "*" + values[numInput - 1 - a]);
			//n--;
		}
		
		/*if (numInput % 2 == 0) {
			for (int i = 0; i < numInput/2; i++) {
				sum += (values[i]) * (values[numInput - 1 - i]) * 2;
			}
		} else {
			for (int i = 0; i < numInput/2 + 1; i++) {
				if (i == numInput - 1 - i) {
					sum += (values[i]) * (values[i]);
				} else {
					sum += (values[i]) * (values[numInput - 1 - i]) * 2;
				}
			}
		}*/
		
		//System.out.println(result % 10007);
		System.out.println(result%10007);
	}
}
