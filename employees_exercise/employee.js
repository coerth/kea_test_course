class Employee {
    #cpr;
    #firstName;
    #lastName;
    #department;
    #baseSalary;
    #educationLevel;
    #dateOfBirth;
    #dateOfEmployment;
    #country;
  
    constructor(cpr, firstName, lastName, department, baseSalary, educationLevel, dateOfBirth, dateOfEmployment, country) {
      this.cpr = cpr;
      this.firstName = firstName;
      this.lastName = lastName;
      this.department = department;
      this.baseSalary = baseSalary;
      this.educationLevel = educationLevel;
      this.dateOfBirth = dateOfBirth;
      this.dateOfEmployment = dateOfEmployment;
      this.country = country;
    }

    get cpr() {
        return this.#cpr;
    }

    set cpr(value) {
        if (value.length === 10 && !isNaN(value)) {
            this.#cpr = value;
        } else {
            throw new Error("CPR must be exactly 10 digits.");
        }
    }
    
    get firstName() {
        return this.#firstName;
    }

    set firstName(value) {
        if (typeof value !== 'string' || value.length < 1 || value.length > 30) {
            throw new Error("First name must be 1-30 characters.");
        }

        for (let char of value) {
            if (!((char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z') || char === ' ' || char === '-')) {
                throw new Error("First name can only contain letters, spaces, or dashes.");
            }
        }

        this.#firstName = value;
    }

    get lastName() {
        return this.#firstName;
    }
    
    set lastName(value) {
        if (typeof value !== 'string' || value.length < 1 || value.length > 30) {
            throw new Error("Last name must be 1-30 characters.");
        }

        for (let char of value) {
            if (!((char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z') || char === ' ' || char === '-')) {
                throw new Error("Last name can only contain letters, spaces, or dashes.");
            }
        }

        this.#lastName = value;
    }

    get department() {
        return this.#department;
    }

    set department(value) {
        const departments = ['HR', 'Finance', 'IT', 'Sales', 'General Services'];
        if (departments.includes(value)) {
            this.#department = value;
        } else {
            throw new Error("Department must be one of HR, Finance, IT, Sales, or General Services.");
        }
    }

    get baseSalary() {
        return this.#baseSalary;
    }

    set baseSalary(value) {
        if (value >= 20000 && value <= 100000) {
          this.#baseSalary = value;
        } else {
          throw new Error("Base salary must be between 20,000 and 100,000 DKK.");
        }
    }

    get educationLevel() {
        return this.#educationLevel;
    }
      set educationLevel(value) {
        const levels = [0, 1, 2, 3]; // 0 (none), 1 (primary), 2 (secondary), 3 (tertiary)
        if (levels.includes(value)) {
          this.#educationLevel = value;
        } else {
          throw new Error("Education level must be 0 (none), 1 (primary), 2 (secondary), or 3 (tertiary).");
        }
    }

    get dateOfBirth() {
        return this.#dateOfBirth;
    }

    set dateOfBirth(value) {
        const dob = new Date(value.split("/").reverse().join("-"));
        const now = new Date();
        const age = now.getFullYear() - dob.getFullYear();
        if (dob <= now && age >= 18) {
          this.#dateOfBirth = value;
        } else {
          throw new Error("Date of birth must be at least 18 years ago.");
        }
    }

    get dateOfEmployment() {
        return this.#dateOfEmployment;
    }

      set dateOfEmployment(value) {
        const doe = new Date(value.split("/").reverse().join("-"));
        const now = new Date();
        if (doe <= now) {
          this.#dateOfEmployment = value;
        } else {
          throw new Error("Date of employment cannot be in the future.");
        }
    }

    get country() {
        return this.#country;
    }

    set country(value) {
        if (typeof value === 'string') {
          this.#country = value;
        } else {
          throw new Error("Country must be a valid string.");
        }
    }

    getSalary() {
        return this.#baseSalary + (this.#educationLevel * 1220);
    }

    getDiscount() {
        //years of employment * 0.5

        const doe = new Date(this.#dateOfEmployment.split("/").reverse().join("-"));
        const now = new Date();
        const years = now.getFullYear() - doe.getFullYear();
        return years * 0.5;
    }

    getShippingCosts() {
        const FREE_SHIPPING = ['Denmark', 'Sweden', 'Norway'];
        const DISCOUNTED_SHIPPING = ['Iceland', 'Finland'];

        if (FREE_SHIPPING.includes(this.#country)) {
            return 0;
        } else if (DISCOUNTED_SHIPPING.includes(this.#country)) {
            return 0.5;
        } else {
            return 1;
        }
    }
}

module.exports = Employee;