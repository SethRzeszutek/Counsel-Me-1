# CounselMe
### A simple app for accessing and managing patient information
*Using Python, Django, and Docker*

## Steps to Remember
* If you changed any fields that would be stored in the data base you will need to manually fix it or just start a new database
* When starting a new database
	* Before logging in you must enter the container shell and create a super user with `python3 manage.py createsuperuser`
	* I usually use `admin` and `admin` as username and password

## Main Views:
* `login page` - simple login page
	* [x] Styling is functional
	* [x] Account authentication
	* [ ] Different types of users(admin and user)
		* [Reference](https://www.geeksforgeeks.org/python-user-groups-custom-permissions-django/)
	* [ ] Better way to add users
* `user home page` - both an admin and counseler landing page
	* [x] Styling
	* [ ] The admin page manages counselor access to patients as well as other settings
	* [ ] The counselor page allows access to assigned patient(s) information and forms (landing page after logging in?)
* `patient page` - view patient information and contracts
	* `patient index page` - view all patients
		* [x] Styling
		* [x] Select and View
	* `patient create page` - create patient
		* [x] Styling
		* [x] Save Patient
	* `patient detail page` - view patient details
		* [x] Delete
		* [ ] Edit (Works, but not in a modal)
* `form pages` - forms like contracts, questionaires, etc.
	* [ ] Styling
	* [ ] Multiple forms that you can 'attach' to the patient object
* `planner page` - a planner/caleneder page
	* [ ] Styling
	* [ ] Calender/Planner

## Probably Messed Up Planning Graph Thing
![Some sort of Planning](https://i.imgur.com/M0EZe2c.png)

## Questions:
* How do we handle forms?
	* User created?
		* https://github.com/stephenmcd/django-forms-builder
		* https://github.com/barseghyanartur/django-fobi
		* MORE: https://djangopackages.org/grids/g/form-builder/
	* Temporarily Hardcoded?
		* Downside is someone would need to contact us to make changes...
	* Just allow document attachments to customers rather than online form?
		* Possibly still need that as an option.
	* If we go strictly online, then we need a "signing spot" or electronic signature.

## References:
* HIPPA Compliance:
	* [Reference](https://devops.com/make-software-hipaa-compliant/)
* Users:
	* [Reference](https://www.geeksforgeeks.org/python-user-groups-custom-permissions-django/)