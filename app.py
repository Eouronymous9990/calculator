import streamlit as st


def calculate(num1, num2, operation):
    """Perform calculation based on selected operation"""
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        # Handle division by zero
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2


def main():
    # Set page title and header
    st.title("🧮 Simple Calculator")

    # Input for first number
    num1 = st.number_input("Enter first number", value=0.0, format="%.2f")

    # Operation selection
    operation = st.selectbox(
        "Select operation",
        ['Add', 'Subtract', 'Multiply', 'Divide']
    )

    # Input for second number
    num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

    # Calculate button
    if st.button("Calculate"):
        # Perform calculation
        result = calculate(num1, num2, operation)

        # Display result
        st.success(f"Result: {result}")


# Run the app
if __name__ == "__main__":
    main()