precision highp float;

uniform sampler2D panorama;
uniform sampler2D depthMap;

uniform vec3 velocity;

varying vec2 pos;

const float PI = 3.14159265358979323846264;
const int NUM_SAMPLES = 20;

void main()
{
    float depth = texture2D(depthMap, pos)[0];

    float theta = pos.y * PI;
    float phi = pos.x * 2.*PI;

    vec3 p = vec3(sin(theta)*cos(phi),
                  sin(theta)*sin(phi),
                  cos(theta));

    p = normalize((depth*p) - velocity);

    float theta_n = acos(p.z);
    float phi_n = atan(p.y, p.x);
    if(phi_n < 0.)
        phi_n += 2.*PI;

    float theta_t = theta_n;
    float phi_t = phi_n;

    vec4 avg = vec4(0.,0.,0.,0.);
    for(int s=0; s<NUM_SAMPLES; ++s) {
        vec2 texPos = vec2(phi_t / (2.*PI),
                           theta_t / PI);

        avg += texture2D(panorama, texPos) / float(NUM_SAMPLES);

        theta_t += (theta - theta_n)/float(NUM_SAMPLES);
        phi_t += (phi - phi_n)/float(NUM_SAMPLES);
    }

    gl_FragColor = avg;
}
