function performOperation(operation) {
    // Get the values from the input fields
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);

    // Check if the user entered valid numbers
    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById('result').innerText = "Please enter valid numbers!";
        return;
    }

    let result;

    // Perform the operation
    switch (operation) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 === 0) {
                result = "Error! Division by zero.";
            } else {
                result = num1 / num2;
            }
            break;
        default:
            result = "Invalid operation!";
    }

    // Display the result
    document.getElementById('result').innerText = `Result: ${result}`;
}
