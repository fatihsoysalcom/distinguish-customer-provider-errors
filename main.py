def simulate_login_attempt(username, password, simulate_system_issue=False):
    """
    Simulates a login attempt and categorizes potential issues as
    Customer Errors or Provider Errors.

    Customer Errors (Kullanıcı Kaynaklı Hatalar) are due to user input or actions.
    Provider Errors (Sağlayıcı Kaynaklı Hatalar) are due to system issues.
    """

    # --- Check for Customer Errors (Kullanıcı Kaynaklı Hatalar) ---
    # These errors occur due to the user's interaction, input, or understanding.
    # If a customer error is detected, we typically don't proceed to check system health,
    # as the request itself is malformed from the user's side.
    if not username or not password:
        # This is an example of a user not providing required information.
        return "CUSTOMER_ERROR: Missing username or password. Please provide both credentials."
    
    if len(username) < 3 or len(password) < 6:
        # This is an example of a user not following specified input rules (e.g., password policy).
        return "CUSTOMER_ERROR: Username must be at least 3 characters, password at least 6 characters."

    # --- Check for Provider Errors (Sağlayıcı Kaynaklı Hatalar) ---
    # These errors occur due to issues within the service provider's system or infrastructure.
    # We only check for provider errors if no customer errors were found,
    # implying the user's input was valid enough to proceed.
    if simulate_system_issue:
        # This simulates an internal system problem, like a database outage or API failure.
        return "PROVIDER_ERROR: Database connection failed or internal server error occurred."

    # If no errors (customer or provider) were found, the operation is successful.
    return "SUCCESS: Login successful."

# --- Test Cases ---

print("--- Scenario 1: Customer Error (Missing Credentials) ---")
# User provides incomplete data.
print(simulate_login_attempt("", "password123"))

print("\n--- Scenario 2: Customer Error (Invalid Password Length) ---")
# User provides data that doesn't meet requirements.
print(simulate_login_attempt("testuser", "short"))

print("\n--- Scenario 3: Provider Error (System Issue) ---")
# User provides valid data, but the system itself has an issue.
print(simulate_login_attempt("validuser", "validpass123", simulate_system_issue=True))

print("\n--- Scenario 4: Successful Login ---")
# User provides valid data, and the system is healthy.
print(simulate_login_attempt("validuser", "validpass123"))

print("\n--- Scenario 5: Both (Customer error takes precedence) ---")
# Even if a system issue is simulated, the customer error is caught first
# because input validation typically precedes backend service calls.
print(simulate_login_attempt("", "short", simulate_system_issue=True))
