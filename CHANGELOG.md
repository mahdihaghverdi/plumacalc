- `v1.4.1`
  - bump to version `v1.4.1`
  - make the histories shown in descending order and remove `new` badge

- `V1.4.0`
  - bump to version `v1.4.0`
  - Write a fabulous README.md for the project;
  - apply the update of `postfixcalc` to project;
  - Update `postfixcalc` and add str_repr_timeout to HeavyInputForm;

- `v1.3.0`
  - bump to version `v1.3.0`
  - postfix and error cards now have copyable content;
  - expression input now has a help_text and a placeholder;
  - When the error is `Wrong Input` the Error card will show the input of the user;
  - remove the `with postfix` button from navbar and create a Checkbox for that;

- `v1.2.1`
  - bump to version `v1.2.1`
  - add copy button to `Answer` section

- `v1.2.0`
  - bump to version `v1.2.0`
  - Update postfix calc and rewrite calculate view;
  - Define HeavyInputFrom form and create a button for its url and test the view in "GET" request;
  - make the links in the navbar look like beautiful buttons and add `heavy calculations` buttons there;
  - refactor index.html and separate different parts and write them in separate html files;

- `v1.1.2`
  - bump to version `v1.1.2`
  - make parameters of calculate funcview keyword only;
  - Extract buttons group of html tags into a separate html file;

- `v1.1.1`
  - bump to version `v1.1.1`
  - apply the resigned history section to `history/`

- `v1.1.0`
  - Bump to version `v1.1.0`
  - Copy buttons are now working nicely WITH the errors included;
  - errors are shown nicely in index.html history section;
  - make `answer` nullable;
  - add a nullable filed to History: `errors`;
  - Update postfixcalc and capture the TimeoutError raised by the lib;

- `v1.0.1`
  - add title for `history/`

- `v1.0.0`
  - make the `/history` much better UI and UX;
  - transfer front page from flex to grid;
  - redesign history section and put copying button for it;
  - redesign Answer Postfix and Errors;
  - redesign the front page;
  - add a badge to history;
  - make icons better and more beautiful;
  - add icons to alerts and change some;
  - separate navbar html code and create a new navbar for history.html;
  - make styling of history.html much better;
  - Add beautiful icons for buttons;
  - Add the history url and view and template to show the full history of the calculations;
  - Fix the bug caused by `button behaviour` of button tags which is `type="submit"`;
  - add another field to history;
  - separate `with_postfix` calculations;
  - define History model and migrate;
  - now you can choose whether to calculate with the postfix shown or not;
  - Calculations and history now have a better bg;
  - all buttons have the appropriate function assigned;
  - write functions for `C` and `CE` buttons;
  - Redesign the front-end;
  - Update `postfixcalc` and use the new API;
  - Play around the front-end of the plumacalc. Add a navbar and divide the main display to content and sidebar;
  - add a better error handling system for the calculator;
  - Customize `input` widget;
  - Add bootstrap to base.html;
  - update postfixcalc to its latest version;
  - calculator is basically working;
  - Define calculate funcview;
  - Define InputForm;
  - startapp calculator;
  - Install postfixcalc;
  - Add poetry.lock to .gitignore, add CHANGELOG.md, .pre-commit-config.yaml and .flake8;
  - Initial commit: django startproject;
  - write out gitignore;
