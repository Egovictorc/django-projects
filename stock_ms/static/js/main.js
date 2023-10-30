import { CountUp } from 'countup.js';

windows.onload = function () {

    const salesCount = document.getElementById("sales-count");
    const demo = new CountUp(salesCount, 1000,  {enableScrollSpy: true });
}