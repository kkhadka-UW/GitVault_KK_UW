import sys
import class_Street as cS
import class_Line as cL
import function_intersection as fi


class Database(object):

    def __init__(self, street_db=None, intersections=None, vertices=None, edges=None):
        if street_db is not None and vertices is not None and edges is not None and intersections is not None:
            self.street_db = street_db
            self.intersections = intersections
            self.vertices = vertices
            self.edges = edges
        else:
            self.street_db = []
            self.intersections = []
            self.vertices = []
            self.edges = []

    def display_intersections(self):
        intersections = self.intersections
        sys.stdout.write('I = {\n')
        for ind in range(len(intersections)):
            sys.stdout.write('  ' + str(intersections[ind][0]) + ': ' + str(intersections[ind][1]) + '\n')
        sys.stdout.write('}\n')

    def display_vertices(self):
        vertices = self.vertices
        sys.stdout.write('V = {\n')
        for ind in range(len(vertices)):
            sys.stdout.write('  ' + str(vertices[ind][0]) + ': ' + str(vertices[ind][1]) + '\n')
        sys.stdout.write('}\n')

    def display_edges(self):
        sys.stdout.write('E = {\n')
        l = len(self.edges)
        for i, e in self.edges:
            sys.stdout.write('  <' + str(int(e[0])) + ',' + str(int(e[1])) + '>')
            if i != l:
                sys.stdout.write(',\n')
            else:
                sys.stdout.write('\n')
        sys.stdout.write('}\n')

    def find_vertices_and_edges(self):
        line_segments = []

        pseudo_street = copy_street(self.street_db)
        intersections = []  # [first_second, first_third,..,first_last, second_third,..second..last,..second_last_last
        vertices = []
        to_update = []

        for street in pseudo_street:
            line_segment = []
            street_points = street.street_point
            for j in range(len(street_points) - 1):
                line_segment += [cL.Line(street_points[j], street_points[j + 1])]  # line segments of single road
            line_segments += [line_segment]  # line segments of all roads
        # find intersections
        for kk in range(0, len(line_segments) - 1):
            for ll in range(kk + 1, len(line_segments)):
                temp = []
                temp_ver = []
                for mm in range(len(line_segments[kk])):
                    l1 = line_segments[kk][mm]
                    for nn in range(len(line_segments[ll])):
                        l2 = line_segments[ll][nn]
                        int_sec, flag = fi.intersection(l1, l2)
                        temp += [int_sec]
                        if flag == 0:
                            # update format intersectin count, line1 no, pa,pb of line1, line2, pa, pb of line 2, int_sec
                            to_update += [[kk, mm, ll, nn, int_sec]]
                            temp_ver += [l1.ipt, l1.fpt, l2.ipt, l2.fpt]
                vertices += temp_ver
                intersections += temp

        intersections = find_unique_points(list_to_set(intersections))
        for a in range(len(intersections)):
            item = [a + 1, intersections[a]]
            self.intersections += [item]

        vertices = find_unique_points(list_to_set(vertices) + intersections)
        for b in range(len(vertices)):
            item = [b + 1, vertices[b]]
            self.vertices += [item]

        #self.update_db(to_update)
        i_counter = []
        for xx in range(len(pseudo_street)):
            i_counter += [0]

        for l1, pl1, l2, pl2, i_s in to_update:
            for j in range(len(pseudo_street)):
                if l1 == j:
                    i_counter[j] += 1
                if l2 == j:
                    i_counter[j] += 1

            temp1 = pseudo_street[l1].street_point
            for pt in temp1:  # check if int_sec is a point already in the road1
                if pt.x_cor != i_s.x_cor or pt.y_cor != i_s.y_cor:
                    state1 = False
                else:
                    state1 = True
                    break

            if not state1:
                temp = pseudo_street[l1].street_point[:pl1 + i_counter[l1]] + [i_s] + pseudo_street[
                                                                                           l1].street_point[
                                                                                       pl1 + i_counter[l1]:]
                pseudo_street[l1].street_point = temp

            temp2 = pseudo_street[l2].street_point
            for pt in temp2:  # check if already in the road1
                if pt.x_cor != i_s.x_cor or pt.y_cor != i_s.y_cor:
                    state2 = False
                else:
                    state2 = True
                    break

            if not state2:
                temp = pseudo_street[l2].street_point[:pl2 + i_counter[l2]] + [i_s] + pseudo_street[
                                                                                           l2].street_point[
                                                                                       pl2 + i_counter[l2]:]
                pseudo_street[l2].street_point = temp
        # now find edges
        e = []
        count = 0
        for width in range(len(pseudo_street)): # for all individual street
            points = pseudo_street[width].street_point
            for aa in range(len(points)-1): # for a point in an individual street
                a_point = points[aa]
                b_point = points[aa+1]

                c1, index_a = self.check_if_vertex(a_point)
                c2, index_b = self.check_if_vertex(b_point)
                c3 = self.check_if_intersection(a_point)
                c4 = self.check_if_intersection(b_point)

                if (c1 and c2) and (c3 or c4):
                    count += 1
                    e += [[count, (index_a, index_b)]]
                self.edges = e

    def check_if_intersection(self, a_point):
        for ind, i_s in self.intersections:  # take a point and check if is intersection
            if a_point.x_cor == i_s.x_cor and a_point.y_cor == i_s.y_cor:
                return True
        return False

    def check_if_vertex(self, b_point):
        for ind, v in self.vertices:
            if b_point.x_cor == v.x_cor and b_point.y_cor == v.y_cor:
                return True, ind
        return False, 0

    def add_street_db(self, street_new):
        found = False
        if len(self.street_db) > 0:
            for iteration in range(len(self.street_db)):
                if self.street_db[iteration].street_name == street_new.street_name:
                    found = True
                    break
                else:
                    found = False
            if found:
                raise Exception('Error: Street already exists.')
            else:
                self.street_db += [street_new]
        else:
            self.street_db += [street_new]
        self.intersections = []
        self.vertices = []
        self.edges = []

    def change_street_db(self, street_new):
        found = False
        iteration = 0
        for iteration in range(len(self.street_db)):
            if self.street_db[iteration].street_name == street_new.street_name:
                found = True
                break
            else:
                found = False
        if found:
            self.street_db[iteration].street_point = street_new.street_point
        else:
            raise Exception('Error: Street does not exist. Street not removed.')
        self.intersections = []
        self.vertices = []
        self.edges = []

    def remove_street_db(self, street_name):
        found = False
        iteration = 0
        for iteration in range(len(self.street_db)):
            if self.street_db[iteration].street_name == street_name:
                found = True
                break
            else:
                found = False
        if found:
            self.street_db.remove(self.street_db[iteration])
        else:
            raise Exception('Error: Street does not exist. Street not removed.')
        self.intersections = []
        self.vertices = []
        self.edges = []

    def create_graph(self):
        self.find_vertices_and_edges()
        #self.display_intersections()
        self.display_vertices()
        self.display_edges()

    def __repr__(self):
        return '\nThe streets are \n [' + str(self.street_db) + ']\nThe vertices are \n[' + \
               str(self.vertices) + ']\nThe edges are \n[' + str(self.edges) + ']\n'


def list_to_set(input_list):
    output_set = []
    for j in range(len(input_list)):
        element = input_list[j]
        if element.x_cor is not None and element.y_cor is not None:
            output_set += [element]
    return output_set


def find_unique_points(all_points):
    # eliminate redundant points
    if len(all_points) <= 1:
        all_unique_points = all_points
    else:
        all_unique_points = [all_points[0]]
        for a_point in all_points:
            for b_point in all_unique_points:
                if a_point.x_cor == b_point.x_cor and a_point.y_cor == b_point.y_cor:
                    break
                else:
                    if b_point != all_unique_points[-1]:
                        continue
                    else:
                        all_unique_points += [a_point]
    return all_unique_points


def copy_street(s_db):
    sn = []
    for nn in range(len(s_db)):
        name = s_db[nn].street_name
        n = s_db[nn].street_point
        xx = cS.Street(name, n)
        sn += [xx]
    return sn