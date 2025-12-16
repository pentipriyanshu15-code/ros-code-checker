                                                   DOCUMENTATION (README)
1. Setup Instructions
System Requirements:
 Ubuntu 20.04
 Python 3
 ROS Noetic
 Git
Required Software Installation:
 Python3
 pip3
 Flask
 Pillow
 ROS Noetic
To prepare the environment:
 Install Python dependencies such as Flask and Pillow.
 Ensure Git is installed for version control.
 Source the ROS setup file before running ROS-related scripts.
The development and testing were done completely on Ubuntu Linux.

2. How to Run the Tool
Step 1: Clone the Project Repository
 Clone the GitHub repository to your local system.
 Navigate into the project folder.
Step 2: Run the Code Checker
 Go to the “checker” directory.
 Execute the Python script to validate ROS ZIP packages.
 Provide the path to the ZIP file when prompted (for example: good.zip or bad.zip).
The code checker verifies:
 Python syntax
 ROS node initialization
 Presence of publishers or subscribers
 Basic safety structure
Step 3: Run the Simulation
 Navigate to the “simulator” directory.
 Run the simulation script.
 The simulation generates logs and a screenshot as output.
Step 4: Run the Web Interface
 Navigate to the “web” directory.
 Start the Flask application.
 Open a web browser and access the local server.
 Upload the ROS ZIP package using the interface to view results.

3. Logs and Notes from Testing
Test Case 1: Correct ROS Package (Pick-and-Place)
Package Name: good.zip
Description:
 Contains a valid ROS node.
 Proper ROS initialization using rospy.
 Implements a pick-and-place sequence.
Checker Results:
 Syntax check passed.
 ROS structure validation passed.
Simulation Output:
 Home
 Pick
 Lift.
 Place
Result:
 The package passed all validation checks.
 Simulation executed correctly.
 Logs and screenshot were generated.
Test Case 2: Faulty ROS Package
Package Name: bad.zip
Description:
 Contains an invalid ROS node.
 Missing rospy.init_node().
 No publisher or subscriber defined.
Checker Results:
 Syntax check passed.
 ROS structure validation failed.
 Errors correctly identified by the checker.
Simulation Output:
 Simulation was not executed due to validation failure.
Result:
 The tool correctly detected errors.
 Faulty code was prevented from running in simulation.

4. Conclusion
The developed tool successfully validates ROS code, differentiates between correct and faulty
packages, and executes simulations only for valid ROS nodes. The project meets all assignment
requirements by including code validation, simulation execution, and a minimal web-based
interface for user interaction.
