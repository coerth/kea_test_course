//jest tests for employee.js

const Employee = require('./employee');

describe('Employee', () => {
    let employee;
    beforeAll(() => {
        employee = new Employee('1234567890', 'John', 'Doe', 'HR', 50000, 3, '01-01-1970', '01-01-2020', 'USA');
    });

    test.each([
        ['0000000000'], // Lower boundary
        ['9999999999'], // Upper boundary
        ['1234567890'], // Middle value
    ])('should set valid CPR %s', (validCPR) => {
        employee.cpr = validCPR;
        expect(employee.cpr).toBe(validCPR);
    });

    test('should throw error for invalid CPR', () => {
        expect(() => {
            employee.cpr = '123456789';
        }).toThrow('CPR must be exactly 10 digits.');
    });

    test('should throw error for invalid first name', () => {
        expect(() => {
            employee.firstName = 'John123';
        }).toThrow('First name can only contain letters, spaces, or dashes.');
    });

    test('should throw error for invalid last name', () => {
        expect(() => {
            employee.lastName = 'Doe123';
        }).toThrow('Last name can only contain letters, spaces, or dashes.');
    });
});