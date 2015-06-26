---vertex shader---------------------------------------------------------------
$HEADER$
attribute vec2 vCenter;
attribute float vScale;
attribute vec3 vColor;

void main() {
    tex_coord0 = vTexCoords0;
    frag_color = vec4(vColor.rgb, 1.0);

    mat4 move_mat = mat4(
        vec4(1.0, 0.0, 0.0, vCenter.x),
        vec4(0.0, 1.0, 0.0, vCenter.y),
        vec4(0.0, 0.0, 1.0, 0.0),
        vec4(0.0, 0.0, 0.0, 1.0)
    );
    vec4 pos = vec4(vPosition.xy * vScale, 0.0, 1.0) * move_mat;
    gl_Position = projection_mat * modelview_mat * pos;
}

---fragment shader-------------------------------------------------------------
$HEADER$

void main() {
    gl_FragColor = frag_color * texture2D(texture0, tex_coord0);
    if (gl_FragColor.rgb == vec3(0.0, 0.0, 0.0)) {
        discard;
    }
}
