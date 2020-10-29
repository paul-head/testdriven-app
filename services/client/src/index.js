import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';


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
                        {
                            this.state.users.map((user) => {
                                return (
                                    <h4
                                        key={user.id}
                                        className="card card-body bg-light">
                                        {user.username}
                                    </h4>
                                )
                            })
                        }

                    </div>
                </div>
            </div>
        )
    };
    }


ReactDOM.render(
  <React.StrictMode>
    <App />,
  </React.StrictMode>,
  document.getElementById('root')
);

