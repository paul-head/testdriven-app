import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import UsersList from "./components/UsersList";


class App extends Component {
    constructor() {
        super();
        this.state = {
            users: []
        };
    };
    componentDidMount() {
        this.getUsers();
    }

    getUsers() {
        axios.get('http://localhost:5001/users')
            .then((res) => { console.log(res); this.setState( { users: res.data.data.users }); })
            .catch((err) => { console.log(err); });
    }

    render() {
        return (
            <div className="container">
                <div className="row">
                    <div className="col-md-6">
                        <br/>
                        <h1>All Users</h1>
                        <hr/><br/>
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

