precision highp float;

attribute vec4 position;

varying vec2 pos;

void main()
{
    pos.x = (position.x + 1.) / 2.;
    pos.y = (position.y + 1.) / 2.;

    gl_Position = vec4(position.x, position.y, -1, 1);
}
