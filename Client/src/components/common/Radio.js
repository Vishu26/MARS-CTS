import React from 'react'

const Radio = (props) => {

    return (
        <div className="RadioInput form-group row">
            {/* <label for="exampleInputEmail1">{props.label}</label> */}
            <div className="col-1">
                <input
                    type={props.type}
                    name={props.name}
                    value={props.value}
                    onChange={props.onChange}
                    className="form-control"
                    aria-describedby="emailHelp"
                    placeholder={props.placeholder} />
            </div>
            <div className="col-11">
                {props.radioMessage}
                <small id="emailHelp" className="form-text text-muted"> {props.message}</small>
                <small id="emailHelp" className="form-text text-muted"> {props.error}</small>
            </div>

        </div>
    )
}

export default Radio;
