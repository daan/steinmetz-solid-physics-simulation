// CSG.scad - Basic example of CSG usage



intersection() {
    cylinder(2,0.5,0.5, center=true, $fn=72);
    rotate([0,90,0]) {
        cylinder(2,0.5,0.5, center=true, $fn=72);
    }
    rotate([90,0,0]) {
        cylinder(2,0.5,0.5, center=true, $fn=72);
    }

}

