import React from "react";
import './applications.css';
import Menu from "../../component/menu/Menu";
import HeaderApplications from "../../component/header/header-applications/Header-applications";
import ApplicationsItem from "../../component/applications-item/ApplicationsItem";

function Applications() {

	return (
		<div className="applications">
			<Menu></Menu>
			<div className="applications__content">
				<div className="applications__content__width">
					<HeaderApplications></HeaderApplications>
					<ApplicationsItem></ApplicationsItem>
				</div>
			</div>
		</div>
	)

}

export default Applications;