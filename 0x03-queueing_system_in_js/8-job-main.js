import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();
const list = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: '4562 to verify your account',
  },
];

before(() => queue.testMode.enter());
afterEach(() => queue.testMode.clear());
after(() => queue.testMode.exit());

test('should create a new job', () => {
  createPushNotificationsJobs(list, queue);
  expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  expect(queue.testMode.jobs.length).to.equal(2);
});

test('if jobs is not an array', () => {
  expect(() => {
    createPushNotificationsJobs(5, queue);
  }).to.throw('Jobs is not an array');
});
