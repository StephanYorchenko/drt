import React, { Component } from "react";
import {Navbar, Nav, NavDropdown} from 'react-bootstrap'

export class NavBar extends Component {
    constructor(props) {
        super(props);
        let loginManager = props.loginManager().setNav(this)
        console.log(loginManager)
        this.state = {
            isOpen: false,
            user: (loginManager.user !== null) ? loginManager.user.name : "Stephan Yorchenko",
            loginManager: loginManager
        };
    }

    hide(){
        this.setState({isOpen: false})
    }

    setUser(user){
        this.setState({
            isOpen: this.state.isOpen,
            user: user.name,
            loginManager: this.state.loginManager
        })
    }

    render() {
        return (
            <Navbar bg="dark" expand="lg" sticky="top">
                <Navbar.Brand href="/" className="text-white">DoubleRT</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        <Nav.Link href="/" className="text-white">Главная</Nav.Link>
                        <Nav.Link href="/request" className="text-white">Заявки</Nav.Link>
                        <Nav.Link href="/request_table" className="text-white">Бронировние</Nav.Link>
                        {this.state.loginManager.isAdmin() && <Nav.Link href="/admin" className="text-white">Администрирование</Nav.Link>}
                    </Nav>
                    <Nav>
                        <NavDropdown title={this.state.user} id="basic-nav-dropdown" menuAlign={{ lg: 'right' }} className="text-white">
                            <NavDropdown.Item onClick={() => this.state.loginManager.clearUser()}>Выход</NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        );
    }
}