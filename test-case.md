# Test Cases for Login Functionality

## Test Case 1: Valid Login
- **ID**: Login_01
- **Description**: Verify user can log in with correct credentials
- **Preconditions**: User has valid username/password in database.
- **Steps**:
  1. Navigate to login page
  2. Enter "Admin" and "admin123"
  3. Click Login
- **Expected Result**: Website is redirected to dashboard page.
- **Actual Result**: Website is redirected to dashboard page
- **Status**: Successs

## Test Case 2: Invalid Login
- **ID**: Login_02
- **Description**: Verify user cannot log in with incorrect credentials
- **Preconditions**: None
- **Steps**:
    1. Navigate to login page
    2. Enter "wrongUser" and "wrongPassword"
    3. Click Login
- **Expected Result**: Website stays on same page, but shows Invalid credentials error.
- **Actual Result**: Same as expected result.
- **Status**: Successs

## Test Case 3: Change Password
- **ID**: Password_Change_01
- **Description**: Verify user can change password
- **Preconditions**: User is already in dashboard
- **Steps**:
    1. Go to user dropdown tab in top right corner.
    2. Select Change Password
    3. Fill in Current Password, New Password, Confirm New Password text fields
    4. Click save
- **Expected Result**: Password changed successfully alert box.
- **Actual Result**: NA
- **Status**: Not Yet Developed






 
