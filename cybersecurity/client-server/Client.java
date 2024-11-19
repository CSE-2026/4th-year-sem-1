import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 12345)) {
            PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            String capitalLetter = "A";
            output.println(capitalLetter);

            String response = input.readLine();
            System.out.println("Received from server: " + response);

        } catch (UnknownHostException e) {
            System.out.println("Unknown host");
            System.out.println(e.getMessage());
        } catch (IOException e) {
            System.out.println("I/O error");
            System.out.println(e.getMessage());
        }
    }
}
