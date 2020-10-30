import React from 'react';
import renderer from 'react-test-renderer';
import { shallow } from 'enzyme';
import UsersList from "../UsersList";

const users = [
    {
        "active": true,
        "email": "pavel@pavel.ru",
        "id": 1,
        "username": "pavel"
    },
    {
        "active": true,
        "email": "testuser1@testuser1.com",
        "id": 2,
        "username": "testuser1"
    },
];


test('UsersList render properly', () => {
    const wrapper = shallow(<UsersList users={users}/>);
    const element = wrapper.find('h4');
    expect(element.length).toBe(2);
    expect(element.get(0).props.className).toBe('card card-body bg-light');
    expect(element.get(0).props.children).toBe('pavel')
});


test('UsersList renders a snapshot properly', () => {
    const tree = renderer.create(<UsersList users={users}/>).toJSON();
    expect(tree).toMatchSnapshot();
})
