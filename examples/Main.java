import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String test = "I'am sad";
		
		
		ProcessBuilder pb = new ProcessBuilder( "/home/amira/miniconda2/bin/python","~/Desktop/deepmoji2/emoji_predictor.py",""+test);
		try{
			Process p = pb.start();
			BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream()));
			String line = "";
			
			System.out.println("pre");
			
			while((line = br.readLine()) != null){
				
				System.out.println("Python: "+ line);
			}
			System.out.println("after");
		}catch(IOException e){
			e.printStackTrace();
		}
	}

}

