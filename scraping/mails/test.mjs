import validate from 'deep-email-validator'
// import { validate } from 'index'
// validate.validate()
// validate.validate(Chaz.Brooks@gmail.com);
const main = async () => {
  let res = await validate.validate('muneeralaali@hotmail.de')
  console.log(res.validators.mx)
  // {
  //   "valid": false,
  //   "reason": "smtp",
  //   "validators": {
  //       "regex": {
  //         "valid": true
  //       },
  //       "typo": {
  //         "valid": true
  //       },
  //       "disposable": {
  //         "valid": true
  //       },
  //       "mx": {
  //         "valid": true
  //       },
  //       "smtp": {
  //         "valid": false,
  //         "reason": "Mailbox not found.",
  //       }
  //   }
  // }

  // Can also be called with these options
//   await validate({
//     email: 'Chaz.Brooks@gmail.com',
//     sender: 'amoussaouianas@gmail.com',
//     validateRegex: true,
//     validateMx: true,
//     validateTypo: true,
//     validateDisposable: true,
//     validateSMTP: true,
//   }).validateDisposable
}
main()