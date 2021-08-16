const menu = {
  _courses: {
    _appetizers: [],
    _mains: [],
    _desserts: [],
    get appetizers() {
      return this._appetizers;
    },
    set appetizers(appetizersIn) {
      this._appetizers = appetizersIn;
    },
    get mains() {
      return this._mains;
    },
    set mains(mainsIn) {
      this._mains = mainsIn;
    },
    get desserts() {
      return this._desserts;
    },
    set desserts(dessertsIn) {
      this._desserts = dessertsIn;
    },
  },
  get courses() {
    return {
      appetizers: this._courses.appetizers,
      mains: this._courses.mains,
      desserts: this._courses.desserts,
    };
	},
  addDishToCourse (courseName, dishName, dishPrice) {
    const dish = {
      name: dishName,
      price: dishPrice,
    };
    this._courses[courseName].push(dish);
  },
  getRandomDishFromCourse(courseName) {
    const dishes = this._courses[courseName];
    const randomIndex = Math.floor(Math.random() * dishes.length);
    return dishes[randomIndex];
  },
  generateRandomMeal() {
    const appetizer = this.getRandomDishFromCourse('appetizers');
    const main = this.getRandomDishFromCourse('mains');
    const dessert = this.getRandomDishFromCourse('desserts');
    const totalPrice = appetizer.price + main.price + dessert.price;
    
    return `You're having ${appetizer.name} as an appetizer, ${main.name} for your main meal, and ${dessert.name} for dessert. Your total will be $${totalPrice.toFixed(2)}.`;
  },
};

menu.addDishToCourse("appetizers", "basmati rice with steamed vegetables", 6.50);
menu.addDishToCourse("appetizers", "chicken tikka", 3.50);
menu.addDishToCourse("appetizers", "yogurt with honey", 5.75);

menu.addDishToCourse("mains", "dal makhany", 12.50);
menu.addDishToCourse("mains", "red curry soup", 9.15);
menu.addDishToCourse("mains", "yellow curry with sweet potato", 12.50);

menu.addDishToCourse("desserts", "rice pudding", 3.75);
menu.addDishToCourse("desserts", "dates with cherries", 3.50);

console.log(menu.courses);

console.log(menu.generateRandomMeal());


