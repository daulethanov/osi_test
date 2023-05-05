import React, { useEffect, useState } from "react";
import './applicationsItem.css';
import SubmitYourApplication from "./submitYourApplication/SubmitYourApplication";
import Board from "./board/Board";

function ApplicationsItem() {

	const applicationsItems = ['Список', 'Доска', 'Оставить заявку'];
	const [applicationsItemsActive, setApplicationsItemsActive] = useState(0);
	


	return (
		<div className="applications__item">
			<ul>
				{applicationsItems.map((applicationsItems, index) => (
					<li key={index} onClick={() => setApplicationsItemsActive(index)} className={applicationsItemsActive === index ? "applications__item  active" : "applications__item "}>{applicationsItems}</li>
				))}
			</ul>
			{applicationsItemsActive === 0 ? (
				1
			) : applicationsItemsActive === 1 ? (
				<Board></Board>
			) : applicationsItemsActive === 2 ? (
				<SubmitYourApplication></SubmitYourApplication>
			) : ('')}
		</div>
	)

}

export default ApplicationsItem;