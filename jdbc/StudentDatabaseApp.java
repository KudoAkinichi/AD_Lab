import java.sql.*;
import java.util.Scanner;

public class StudentDatabaseApp {
    private Connection connection;

    public StudentDatabaseApp() {
        try {
            String connectionString = "jdbc:mysql://localhost:3306/cs28";
            String username = "root";
            String password = "SilverhitX88";
            connection = DriverManager.getConnection(connectionString, username, password);
            System.out.println("Connected to database successfully");
        } catch (SQLException e) {
            System.err.println("Error connecting to database: " + e.getMessage());
        }
    }

    public void addStudent(String rollNo, String name) {
        if (!rollNo.isEmpty() && !name.isEmpty()) {
            try {
                PreparedStatement statement = connection
                        .prepareStatement("INSERT INTO students (rollno, name) VALUES (?, ?)");
                statement.setString(1, rollNo);
                statement.setString(2, name);
                statement.executeUpdate();
                System.out.println("Student added successfully.");
            } catch (SQLException ex) {
                System.err.println("Error inserting data: " + ex.getMessage());
            }
        } else {
            System.out.println("Roll number and name cannot be empty.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StudentDatabaseApp app = new StudentDatabaseApp();

        while (true) {
            System.out.println("\nWelcome to Student Database Application");
            System.out.println("1. Add Student");
            System.out.println("2. Exit");
            System.out.print("Choose an option: ");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    System.out.print("Enter Roll No: ");
                    String rollNo = scanner.nextLine();
                    System.out.print("Enter Name: ");
                    String name = scanner.nextLine();
                    app.addStudent(rollNo, name);
                    break;
                case 2:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}