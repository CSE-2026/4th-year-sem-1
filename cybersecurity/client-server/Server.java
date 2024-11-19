import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(12345)) {
            System.out.println("Server is listening on port 12345");

            while (true) {
                try (Socket socket = serverSocket.accept()) {
                    System.out.println("Client connected");

                    BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                    PrintWriter output = new PrintWriter(socket.getOutputStream(), true);

                    String capitalLetter = input.readLine();
                    if (capitalLetter != null) {
                        String lowerCaseLetter = capitalLetter.toLowerCase();
                        output.println(lowerCaseLetter);
                    }
                } catch (IOException e) {
                    System.out.println("Exception caught when trying to listen on port 12345 or listening for a connection");
                    System.out.println(e.getMessage());
                }
            }
        } catch (IOException e) {
            System.out.println("Could not listen on port 12345");
            System.out.println(e.getMessage());
        }
    }
}
