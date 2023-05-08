import React from "react";
import './aplicationsInput.css';

function AplicationsInput(props) {

	return (
		<input
			className="application__form__left__input"
			type="text"
			value={props.value}
			onChange={props.onChange}
			placeholder={props.placeholder}
			maxLength={props.maxLength}
		></input>
	)

}

export default AplicationsInput;