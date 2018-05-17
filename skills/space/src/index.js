
function main(args) {
    const payload = args.payload || {};
    return { payload: space(payload) };
}

function space(payload) {
    const leftPad = require("left-pad")

    // get text from payload
    const text = payload.text || "(silence)";

    // compute output
    var space_text = "";
    for(let i = 0; i < text.length; i++){
        space_text += text[i] + "   ";
    }

    return { text: leftPad(space_text, 30) };
}

exports.main = main;
