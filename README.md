<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Szezi/KinematicsSolverApp">
    <img src="data\images\icons8-robot-50.png" alt="Logo" width="50" height="50">
  </a>
<h3 align="center">KinematicsSolverApp</h3>
  <p align="center">
KinematicsSolverApp is a desktop application that allows to perform forward and inverse kinematics calculations using D-H and geometrical methods.
    <br />
    <a href="https://github.com/Szezi/ManipulatorApp"><strong>Explore the docs »</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
      <ul>
        <li><a href="#technologies">Technologies</a></li>
      </ul>
    </li>
    <li><a href="#about-the-project">About the project</a></li>
      <ul>
        <li><a href="#desktop-app">Desktop App</a></li>
      </ul>
      <ul>
        <li><a href="#unit-tests">Unit tests</a></li>
      </ul>
    <li><a href="#todo">Todo</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- GETTING STARTED -->
## Getting Started

To run this project, create virtual environment and install it locally.

### Installation

1. Clone the repo
   ```sh
   $ git clone https://github.com/Szezi/KinematicsSolverApp
   ```
2. Install packages
   ```sh
   $ pip install -r requirements.txt
   ```
3. Run main.py

### MacOS

In case of using MacOS add in main.py
```sh
import os
os.environ['QT_MAC_WANTS_LAYER'] = '1'
```
Also if there is issue with fonts, change used fonts families in ui_KinematicsSolverApp.py for example to Helvetica.
### Technologies

* [Python](https://www.python.org/downloads/release/python-370/)
* [PySide2](https://pypi.org/project/PySide2/)
* [pytest](https://pypi.org/project/pytest/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ABOUT THE PROJECT -->
## About The Project

KinematicsSolverApp is a desktop application that allows to perform forward and inverse kinematics calculations using D-H and geometrical methods.
### Desktop app
<div align="center">
<img src="data\images\home.PNG" alt="page_Home">
</div>

The desktop application consists of 4 main screens with different functionality. Switching between the selected screens is done with the use of the pull-down side menu. In the upper bar there is information about the currently selected screen, while in the lower part of the screen there is a bar with application operation messages. These logs are also saved in the appropriate file.

<div align="center">
<img src="data\images\FK_INPUT.PNG" alt="page_fk">
</div>

The FK screen is used to calculate the forward kinematics of the manipulator. The application page has 3 tabs. First tab - Input/Solve allows user to input basic data about robotic arm, its links length and joints range. Filling these informations app allows user to solve forward kinematics with given joints values. On this tab Denavit-Hartenberg table is being shown.

<div align="center">
<img src="data\images\FK_MATRICES.PNG" alt="page_fk">
</div>

Second tab - Homogeneous matrices - allows user to see results of performed calculations with created homogeneous matrices.

<div align="center">
<img src="data\images\FK_USER.PNG" alt="page_fk">
</div>

Last tab - User - allows user to calculate forward kinematics with only given by user dh table. In additions this method allows to calculate kinematics with more then 5 transformation simply by adding more rows to the table. Results of calculations are shown on the right side of the page.

<div align="center">
<img src="data\images\IK_INPUT.PNG" alt="page_ik">
</div>

The IK screen is used to calculate the inverse kinematics of the manipulator. The application page has 2 tabs. First tab - Input/Solve allows user to input basic data about robotic arm, its links length and joints range. Filling these informations app allows user to solve inverse kinematics with given xyz values. Results in 2 configurations are shown below. The second tab contains a diagram of the robot arm.

<p align="right">(<a href="#top">back to top</a>)</p>

### Unit tests
<div align="center">
<img src="data\images\TESTS.PNG" alt="page_ik">
</div>

Unit tests to module of forward kinematics (fk_solver) and inverse kinematics (ik_solver) were developed using pytest. 
Unit tests coverage of fk_solver is 94%.
Unit tests coverage of ik_solver is 81%.

<p align="right">(<a href="#top">back to top</a>)</p>
<!-- Todo -->
## Todo

- [ ] Unit tests
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GPL-3.0 license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/Szezi/KinematicsSolverApp](https://github.com/Szezi/KinematicsSolverApp)

<p align="right">(<a href="#top">back to top</a>)</p>
