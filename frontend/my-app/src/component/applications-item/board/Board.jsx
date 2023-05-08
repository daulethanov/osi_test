import React, { useState, useEffect } from "react";
import './board.css';
import axios from 'axios';

function Board() {

	const [applications, setApplications] = useState([])

	useEffect(() => {
		axios.get('http://127.0.0.1/api/v1/problem/list')
			.then(response => {
				setApplications(response.data)
			})
			.catch(error => {
				console.log(error)
			})

	}, [])


	return (
		<div className="board">
			<div className="board__item board__execution">
				<h2>К исполнению</h2>
				<div className="board__item__contnet">
					{applications.map((applications) => (
						<div className="board__applications"
							key={applications.id}
							onClick={() => console.log(applications.title)}>
							<h4>{applications.name} {applications.surname}</h4>
							<h2>{applications.title}</h2>
							<h3>{applications.description}</h3>
							<span key={applications.id} className={
								applications.important === 'Важно' ? "board__applications__important board__applications__important-red" :
									applications.important === 'Второстепенная' ? "board__applications__important board__applications__important-yellow" :
										applications.important === 'Не важно' ? "board__applications__important board__applications__important-green" : ''
							}>{applications.level_problem}</span>
						</div>
					))}
				</div>
			</div>
			<div className="board__item board__work">
				<h2>В работе</h2>
				<div className="board__item__contnet">
					{/* <div className="board__applications">
						<h3>Течёт труба мощно надо срочно...</h3>
						<span className="board__applications__important">
							высокий
						</span>
						<img src="img/header/header-applications/profile.svg" alt="user" />
					</div> */}
				</div>
			</div>
			<div className="board__item board__ready">
				<h2>Готово</h2>
				<div className="board__item__contnet">
					{/* <div className="board__applications">
						<h3>Течёт труба мощно надо срочно...</h3>
						<div className="board__applications__finish">
							<div className="board__applications__finish__left">
								<span className="board__applications__important">
									высокий
								</span>
								<img src="img/header/header-applications/profile.svg" alt="user" />
							</div>
							<div className="board__applications__finish__right">
								<h3>Выполнено</h3>
							</div>
						</div>
					</div> */}
				</div>
			</div>
		</div>
	)

}

export default Board;