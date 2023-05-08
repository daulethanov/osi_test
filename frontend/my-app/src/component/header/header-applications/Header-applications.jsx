import React from "react";
import './header-applications.css';

function HeaderApplications() {

	return (
		<div className="header__applications">
			<div className="header__applications__left">
				<img src="img/header/header-applications/header-logo.svg" alt="header-logo" />
				<h2>Заявки</h2>
			</div>
			<div className="header__applications__right">
				<img id="notifications" src="img/header/header-applications/notifications.svg" alt="notifications" />
				<img src="img/header/header-applications/profile.svg" alt="profile" />
			</div>
		</div>
	)

}

export default HeaderApplications;