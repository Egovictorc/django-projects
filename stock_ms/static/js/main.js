import { CountUp } from './countup.ts';

windows.onload = function () {
    const demo = new CountUp("sales-count", 1000,  {enableScrollSpy: true });
}