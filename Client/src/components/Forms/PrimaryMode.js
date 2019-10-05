import React, { Component } from 'react'
import { Modal, Button } from 'react-bootstrap'

class PrimaryMode extends Component {

    state = {
        show: this.props.show
    }

    handleClose = (e) => {
        e.preventDefautl()
        this.setState({
            show: false
        })
    }

    render() {

        return (
            <div>
                {/* <h1>Select Primary Mode</h1> */}
                <Modal show={this.state.show} onHide={e => this.handleClose(e)}>
                    <Modal.Header closeButton>
                        <Modal.Title>Modal heading</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>Woohoo, you're reading this text in a modal!</Modal.Body>
                    <Modal.Footer>
                        <Button variant="secondary" onClick={e => this.handleClose(e)}>
                            Close
          </Button>
                        {/* <Button variant="primary" onClick={e => this.handleClose(e)}>
                            Save Changes
          </Button> */}
                    </Modal.Footer>
                </Modal>
            </div>
        )
    }
}

export default PrimaryMode