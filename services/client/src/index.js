import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import UsersList from "./components/UsersList";
import AddUser from "./components/AddUser";


class App extends Component {
    constructor() {
        super();
        this.state = {
            users: [],
            username: '',
            email: '',
        };
        this.addUser = this.addUser.bind(this);
        this.handleChange = this.handleChange.bind(this);
    };
    componentDidMount() {
        this.getUsers();
    }

    getUsers() {
        axios.get('http://localhost:5001/users')
            .then((res) => { console.log(res); this.setState( { users: res.data.data.users }); })
            .catch((err) => { console.log(err); });
    }


    addUser(event) {
        event.preventDefault();
        const data = {
            username: this.state.username,
            email: this.state.email,
        };
        axios.post('http://localhost:5001/users', data) // export REACT_APP_USERS_SERVICE_URL
            .then((res) => {
                this.getUsers();
                this.setState({ username: '', email: '' });
            })
            .catch((err) => { console.log(err); });
    };

    handleChange(event) {
        const obj = {};
        obj[event.target.name] = event.target.value;
        this.setState(obj);
    }

    render() {
        return (
            <div className="container">
                <div className="row">
                    <div className="col-md-6">
                        <br/>
                        <h1>All Users</h1>
                        <hr/><br/>
                        <AddUser
                            username={this.state.username}
                            email={this.state.email}
                            handleChange={this.handleChange}
                            addUser={this.addUser}
                        />
                        <br/>
                        <UsersList users={this.state.users}/>
                    </div>
                </div>
                <Button name="axios get again" onClick={() => { this.getUsers() }}/>
            </div>
        )
    };
}


class Button extends Component {
    render() {
        return(
        <button onClick={this.props.onClick}>
            {
                this.props.name
            }
        </button>)
    }
}

ReactDOM.render(
  <React.StrictMode>
    <App />,
  </React.StrictMode>,
  document.getElementById('root')
);

