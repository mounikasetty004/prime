class CustomException extends Exception {
    public CustomException(String message) {
        super(message);
    }
}

public class Customexceptions {
    public static void main(String[] args) {
        try {
            validateNumber(-1);
        } catch (CustomException e) {
            System.out.println("Caught Exception: " + e.getMessage());
        }
    }

    public static void validateNumber(int number) throws CustomException {
        if (number < 0) {
            throw new CustomException("Number cannot be negative!");
        }
        System.out.println("Number is valid: " + number);
    }
}